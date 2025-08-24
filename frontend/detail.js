/** @format */

// Pega o nome do arquivo da URL: ?arquivo=nome.json
const params = new URLSearchParams(window.location.search);
const arquivo = params.get("arquivo");
const detNome = document.getElementById("detNome");
const detSubtitle = document.getElementById("detSubtitle");
const loading = document.getElementById("loading");

// Abas
const tabs = document.querySelectorAll(".tab");
const btns = document.querySelectorAll(".tab-btn");

btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.add("hidden"));
    document.getElementById(btn.dataset.tab).classList.remove("hidden");
    btns.forEach((b) => b.classList.remove("bg-gray-100"));
    btn.classList.add("bg-gray-100");
  });
});

async function carregarConsulta() {
  loading.classList.remove("hidden");

  try {
    const res = await fetch(`http://127.0.0.1:5000/consulta/${arquivo}`);
    const consulta = await res.json();

    detNome.innerText = consulta.clinico.S.identificacao.nome;
    detSubtitle.innerText = consulta.clinico.S.queixa_principal;

    document.getElementById("tabS").innerHTML = `
      <h3 class="font-semibold mb-2">História da Doença Atual</h3>
      <p>${consulta.clinico.S.historia_doenca_atual}</p>
    `;

    document.getElementById("tabO").innerHTML = `
      <h3 class="font-semibold mb-2">Sinais e Sintomas</h3>
      <ul class="list-disc pl-6">
        ${consulta.clinico.O.sinais_sintomas
          .map((s) => `<li>${s}</li>`)
          .join("")}
      </ul>
      <h3 class="font-semibold mt-4 mb-2">Hábitos</h3>
      <ul class="list-disc pl-6">
        <li>Tabagismo: ${consulta.clinico.O.habitos.tabagismo}</li>
        <li>Álcool: ${consulta.clinico.O.habitos.alcool}</li>
        <li>Substâncias: ${consulta.clinico.O.habitos.substancias}</li>
      </ul>
      <h3 class="font-semibold mt-4 mb-2">Histórico Médico</h3>
      <ul class="list-disc pl-6">
        <li>Doenças de infância: ${consulta.clinico.O.historico_medico.doencas_infancia.join(
          ", "
        )}</li>
        <li>Cirurgias: ${consulta.clinico.O.historico_medico.cirurgias}</li>
        <li>Internações: ${consulta.clinico.O.historico_medico.internacoes}</li>
        <li>Familiares: ${consulta.clinico.O.historico_medico.familiares}</li>
      </ul>
      <p class="mt-2"><strong>Atividade Física:</strong> ${
        consulta.clinico.O.atividade_fisica
      }</p>
      <p><strong>Vida Sexual:</strong> ${consulta.clinico.O.vida_sexual}</p>
    `;

    document.getElementById("tabA").innerHTML = `
      <p>${consulta.clinico.A.avaliacao}</p>
    `;

    document.getElementById("tabP").innerHTML = `
      <ul class="list-disc pl-6">
        ${consulta.clinico.P.plano.map((p) => `<li>${p}</li>`).join("")}
      </ul>
    `;

    document.getElementById("tabPaciente").innerHTML = `
      <p class="italic">${consulta.paciente.mensagem}</p>
    `;

    // Mostra a primeira aba
    btns[0].click();
  } catch (err) {
    detNome.innerText = "Erro ao carregar consulta";
    detSubtitle.innerText = err.message;
  } finally {
    loading.classList.add("hidden");
  }
}

carregarConsulta();
