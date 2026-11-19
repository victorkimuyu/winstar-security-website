<?php
declare(strict_types=1);

use PHPMailer\PHPMailer\PHPMailer;

function finish(int $status, string $message): never
{
    header('Cache-Control: no-store');
    if (str_contains($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json')) {
        http_response_code($status);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['sent' => $status === 200, 'message' => $message]);
    } elseif ($status === 200) {
        header('Location: thank-you.html', true, 303);
    } else {
        http_response_code($status);
        header('Content-Type: text/html; charset=utf-8');
        echo '<!doctype html><html lang="en"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Contact Winstar</title><main><p>'
            . htmlspecialchars($message) . '</p><a href="contact_us.html#contact-form">Return to the contact form</a></main></html>';
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Allow: POST');
    finish(405, 'Please use the contact form to send a message.');
}

function field(string $key): string
{
    $value = $_POST[$key] ?? '';
    return is_string($value) ? trim($value) : '';
}

$name = field('name');
$email = field('email');
$phone = field('phone');
$message = field('message');
if ($name === '' || $message === '' || ($email === '' && $phone === '')) {
    finish(422, 'Enter your name, your message and either an email address or a phone number.');
}
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    finish(422, 'Please check your email address.');
}
if (strlen($name) > 500 || strlen($phone) > 100 || strlen($message) > 40000) {
    finish(422, 'Please shorten your entry and try again.');
}

try {
    $autoload = __DIR__ . '/vendor/autoload.php';
    $host = getenv('SMTP_HOST');
    $username = getenv('SMTP_USERNAME');
    $password = getenv('SMTP_PASSWORD');
    $from = getenv('SMTP_FROM') ?: $username;
    if (!is_file($autoload) || !$host || !$username || !$password || !$from) {
        throw new RuntimeException('Missing mail configuration.');
    }
    require $autoload;
    $mail = new PHPMailer(true);
    $mail->isSMTP();
    $mail->Host = $host;
    $mail->SMTPAuth = true;
    $mail->Username = $username;
    $mail->Password = $password;
    $mail->Port = (int) (getenv('SMTP_PORT') ?: 587);
    $mail->SMTPSecure = $mail->Port === 465 ? PHPMailer::ENCRYPTION_SMTPS : PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Timeout = 15;
    $mail->CharSet = 'UTF-8';
    $mail->setFrom($from, 'Winstar website');
    $mail->addAddress('info@winstarsecurity.co.ke');
    if ($email !== '') {
        $mail->addReplyTo($email);
    }
    $mail->Subject = 'Website enquiry';
    $mail->Body = "Name: $name\nEmail: $email\nPhone: $phone\n\n$message";
    $mail->send();
} catch (Throwable $error) {
    error_log('Winstar contact form delivery failed: ' . get_class($error));
    finish(503, 'We couldn’t send your message. Please try again or call our team.');
}
finish(200, 'Message sent.');
