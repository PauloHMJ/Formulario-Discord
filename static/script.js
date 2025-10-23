
const form = document.getElementById("formulario");
const mensagem = document.getElementById("mensagem");


const popupBackdrop = document.getElementById("popupBackdrop");
const closePopup = document.getElementById("closePopup");
const popupCard = document.querySelector(".popup-card");
const popupIcon = document.querySelector(".popup-icon");
const popupText = popupCard.querySelector("p");
const popupTitle = popupCard.querySelector("h3");


function showPopup(tipo = "sucesso", texto = "") {
  if (tipo === "sucesso") {
    popupCard.style.background = "linear-gradient(135deg, #3b82f6, #9333ea)";
    popupIcon.textContent = "✅";
    popupTitle.textContent = "Formulário Enviado!";
    popupText.textContent = texto || "Seus dados foram enviados com sucesso 🎉";
  } else if (tipo === "nick") {
    popupCard.style.background = "linear-gradient(135deg, #f59e0b, #b45309)";
    popupIcon.textContent = "⚠️";
    popupTitle.textContent = "Nick já cadastrado!";
    popupText.textContent = texto || "Este nick do Discord já foi usado.";
  } else {
    popupCard.style.background = "linear-gradient(135deg, #ef4444, #b91c1c)";
    popupIcon.textContent = "❌";
    popupTitle.textContent = "Erro ao enviar!";
    popupText.textContent = texto || "Ocorreu um problema ao enviar o formulário 😥";
  }

  popupBackdrop.classList.add("show");

}

function hidePopup() {
  popupBackdrop.classList.remove("show");
}


closePopup.addEventListener("click", hidePopup);
popupBackdrop.addEventListener("click", (e) => {
  if (e.target === popupBackdrop) hidePopup();
});


form.addEventListener("submit", async (e) => {
  e.preventDefault();
  mensagem.innerHTML = '<p class="sucesso">Verificando nick... ⏳</p>';

  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());
  const nick = data.NickDiscord?.trim();

  if (!nick) {
    mensagem.innerHTML = '<p class="erro">Digite seu nick do Discord.</p>';
    return;
  }

  // --- Verificador de Nick ---
  try {
    const checkRes = await fetch("/verificar-nick", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ NickDiscord: nick }),
    });

    const check = await checkRes.json();

    if (check.existe) {
      mensagem.innerHTML = '<p class="erro">Este nick já foi usado!</p>';
      showPopup("nick");
      return;
    }
  } catch (error) {
    console.error("Erro ao verificar nick:", error);
    mensagem.innerHTML = '<p class="erro">Falha na verificação do nick.</p>';
    showPopup("erro");
    return;
  }

  // --- Enviar formulário ---
  mensagem.innerHTML = '<p class="sucesso">Enviando dados... ⏳</p>';

  try {
    const res = await fetch("/enviar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();

    setTimeout(() => {
      if (result.success) {
        mensagem.innerHTML = "";
        form.reset();
        showPopup("sucesso");
      } else {
        mensagem.innerHTML = '<p class="erro">Erro ao enviar formulário.</p>';
        showPopup("erro");
      }
    }, 1200);
  } catch (err) {
    console.error(err);
    mensagem.innerHTML = '<p class="erro">Erro ao enviar formulário.</p>';
    showPopup("erro");
  }
});
