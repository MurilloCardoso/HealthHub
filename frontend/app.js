/** @format */
async function carregarConsultas() {
  const lista = document.getElementById("lista");
  const vazio = document.getElementById("listaEmpty");
  lista.innerHTML = "";
  vazio.classList.add("hidden");

  const res = await fetch("http://127.0.0.1:5000/consultas");
  const consultas = await res.json();

  if (!consultas.length) {
    vazio.classList.remove("hidden");
    return;
  }

  consultas.forEach((c) => {
    const el = document.createElement("div");
    el.className =
      "p-4 mb-3 border rounded-lg flex justify-between items-center shadow-sm transition-colors duration-150 " +
      (c.status === "processando"
        ? "bg-gray-100 text-gray-400"
        : "bg-white hover:bg-blue-50");

    el.innerHTML = `
      <div>
      <strong class="text-lg text-gray-800">${c.nome}</strong><br>
      <span class="text-sm text-gray-600">${c.queixa}</span>
      </div>
      <div>
      ${
        c.status === "processando"
          ? `<span class="text-base italic flex items-center gap-2">
          <span class="animate-spin inline-block w-4 h-4 border-2 border-blue-400 border-t-transparent rounded-full"></span>
          Em processamento...
          </span>`
          : `<span class="text-green-600 font-semibold">Processada</span>`
      }
      </div>
    `;
    if (c.status !== "processando") {
      el.style.cursor = "pointer";
      el.onclick = () => abrirConsulta(c.arquivo);
    }
    lista.appendChild(el);
  });
}

// Botão refresh
document.addEventListener("DOMContentLoaded", () => {
  carregarConsultas();

  const btnRefresh = document.getElementById("btnRefresh");
  if (btnRefresh) btnRefresh.onclick = carregarConsultas;
});

function abrirConsulta(arquivo) {
  window.location.href = `detail.html?arquivo=${encodeURIComponent(arquivo)}`;
}
