(() => {
    document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star');
    const scoreInput = document.getElementById('id_score');

    stars.forEach(star => {
        star.addEventListener('click', function () {
            const value = this.getAttribute('data-value');
            scoreInput.value = value;
            stars.forEach(s => {
                s.classList.remove('selected');
            });
            this.classList.add('selected');
            this.nextElementSibling?.classList.add('selected');
        });
    });
});

})();                   