const emailInput = document.getElementById('email-input');
const emailSubmit = document.getElementById('email-submit');
const topic = document.querySelectorAll('.topic');
const searchArticle = document.getElementById('search-article');

topic.forEach(tag => {
    if(tag.textContent === 'Sports'){
        tag.className = 'text-danger'
    }

    else if(tag.textContent === 'General'){
        tag.className = 'text-success'
    }

    else if(tag.textContent === 'Events'){
        tag.className = 'text-info'
    }

    else if(tag.textContent === 'Academics'){
        tag.className = 'text-primary'
    }

    else if(tag.textContent === 'Lifestyle'){
        tag.style.color = 'brown'
    }

    else{
        tag.className = 'text-dark'
    }
});


emailSubmit.addEventListener('click', (e) => {
    if(validateEmail(emailInput.value)){
        emailInput.classList.add('border-success');
        emailInput.classList.remove('border-danger');
        console.log(emailInput.value);
        return true;
    }

    else if(emailInput.value === ''){
        emailInput.classList.add('border-danger');
        emailInput.placeholder = 'Email cannot be empty';
        e.preventDefault()
    }

    else{
        emailInput.placeholder = 'Write a real Email';
        emailInput.value = ''
        emailInput.classList.add('border-danger');
        e.preventDefault()
    }
});


function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

searchArticle.addEventListener('keyup', filterItems);
var card = document.querySelectorAll('.col-md-6');

function filterItems(e){
    var text = e.target.value.toLowerCase();  // Get input text

    var cardHeadings = document.querySelectorAll('.my-card-heading');

    Array.from(cardHeadings).forEach(function(heading){
        if(heading.textContent.toLowerCase().indexOf(text) != -1){
            heading.parentNode.parentNode.style.display = 'block';
        }
        else{
            heading.parentNode.parentNode.style.display = 'none';
        }
    });

}

