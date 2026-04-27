// static/admin/js/buscar_cep.js

document.addEventListener('DOMContentLoaded', function () {

    const campoCep = document.querySelector('#id_cep');

    if (!campoCep) return;

    campoCep.addEventListener('blur', async function () {

        const cep = this.value.replace(/\D/g, '');

        if (cep.length !== 8) return;

        try {
            campoCep.style.backgroundColor = '#f0f0f0';

            const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);

            if (!response.ok) {
                throw new Error('Erro na requisição');
            }

            const data = await response.json();

            if (data.erro) {
                alert('CEP não encontrado!');
                return;
            }

            const setValue = (id, value) => {
                const field = document.querySelector(id);
                if (field) field.value = value || '';
            };

            setValue('#id_logradouro', data.logradouro);
            setValue('#id_bairro', data.bairro);
            setValue('#id_cidade', data.localidade);
            setValue('#id_estado', data.uf);

            const numero = document.querySelector('#id_numero');
            if (numero) numero.focus();

        } catch (error) {
            console.error('Erro ao buscar CEP:', error);
            alert('Erro ao consultar o CEP. Tente novamente.');
        } finally {
            campoCep.style.backgroundColor = '';
        }

    });

});