const ctx = document.getElementById('grafico');

new Chart(ctx, {
type: 'bar',

data: {
labels: ['Recursos', 'Usuários'],

datasets: [{
label: 'Dados do Sistema',
data: [10, 5],
backgroundColor: ['gold','gray']
}]
}

});