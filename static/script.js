const form = document.getElementById("formulario");
const mensagem = document.getElementById("mensagem");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  mensagem.innerHTML = '<p class="sucesso">Enviando dados... ⏳</p>';

  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  try {
    const res = await fetch("/enviar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    const result = await res.json();


    setTimeout(() => {
    if(result.success){
      mensagem.innerHTML = '<p class="sucesso">Formulário enviado com sucesso! 🎉</p>';
      form.reset();
    } else {
      mensagem.innerHTML = '<p class="erro">Erro ao enviar formulário.</p>';
    }

  },2000);

  
  } catch(err){
    setTimeout(() => {
    mensagem.innerHTML = '<p class="erro">Erro ao enviar formulário.</p>';
    console.error(err);
    }, 2000);
  }
;



});
