async function botao_1() {
    console.log('teste botão 1')
    eel.bnt_scrap()
};

async function botao_2() {
    console.log('teste botão 2')
    eel.bnt_analise()
};

async function bnt_scrap_corection() {
    console.log('teste botão 3')
    eel.bnt_analise()
};

async function botao_4() {
};


eel.expose(login_return)
function login_return(status) {
    var status = JSON.parse(status);
    eel.change_current_page("configs_1.html");
}