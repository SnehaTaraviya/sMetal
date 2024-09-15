const form = document.querySelector('form');

function sendEmail() {
    Email.send({
        Host : "smtp.gmail.com",
        Username : "info.sneha12401@gmail.com",
        Password : "nvvzhsxzxniowjiz",
        To : 'info.sneha12401@gmail.com',
        From : "iamsneha0412@gmail.com",
        Subject : "New Test Email",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );
}