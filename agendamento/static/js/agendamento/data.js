document.addEventListener("DOMContentLoaded", function () {
    const dateInput = document.querySelector('input[type="date"]');

    dateInput.addEventListener("input", function () {
        const selectedDate = new Date(this.value);
        const dayOfWeek = selectedDate.getUTCDay();

        // Verifica se o dia da semana é sexta (5), sábado (6) ou domingo (0)
        if (dayOfWeek === 5 || dayOfWeek === 6 || dayOfWeek === 0) {
            alert("Por favor, escolha uma data entre segunda e quinta-feira.");
            this.value = ""; // Limpa a seleção inválida
        }
    });
});