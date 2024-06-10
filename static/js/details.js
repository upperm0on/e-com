var labels = document.querySelectorAll('label');

labels.forEach((label, index) => {
    label.addEventListener('click', () => {
        for (var i = 0; i <= index; i++) {
            labels[i].classList.add('active');
        }
        for (var i = index + 1; i < labels.length; i++) {
            labels[i].classList.remove('active');
        }
        updateStars();
    });

    label.addEventListener('mouseenter', () => {
        if (!label.classList.contains('active')) {
            for (var i = 0; i <= index; i++) {
                labels[i].innerHTML = '<i class="fa-solid fa-star"></i>';
            }
        }
    });

    label.addEventListener('mouseleave', () => {
        if (!label.classList.contains('active')) {
            for (var i = 0; i <= index; i++) {
                labels[i].innerHTML = '<i class="fa-regular fa-star"></i>';
            }
        }
    });
});

function updateStars() {
    labels.forEach((label, index) => {
        if (label.classList.contains('active')) {
            label.innerHTML = '<i class="fa-solid fa-star"></i>';
        } else {
            label.innerHTML = '<i class="fa-regular fa-star"></i>';
        }
    });
}
