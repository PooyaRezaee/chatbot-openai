const btn = document.getElementById("BtnSend");
const continer_texts = document.getElementById("container-texts");

btn.addEventListener("click", async () => {
    btn.disabled = true;
    let inp = document.getElementById("message");
    let text = inp.value;
    if (text === "") {
        await addParagraph("Must Enter a Text to Input", (type = "error"));
    } else {
        inp.value = "";
        await addParagraph(text, (type = "self"));
        let response = await send_request(text);
        await set_response(response);
    }
    let hr = document.createElement("hr");
    hr.classList.add("m-5");
    continer_texts.appendChild(hr);
    btn.disabled = false;
});

function handleKeyDown(event) {
    if (event.keyCode === 13) {
        btn.click()
    }
}

async function send_request(text) {
    const response = await fetch('api/chat/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({text: text})
    });

    const data = await response.json();
    if (data.status === 'ok'){
        return {type: 'response',data: data.response};
    }else if (data.status == 'error'){
        return {type: 'error',data: data.msg}
    }else{
        return 'have error';
    }
}

async function set_response(response) {
    const text_response = response.data;
    const type_response = response.type;
    await addParagraph(text_response,type=type_response);
}

async function addParagraph(text, type = "response") {
    return new Promise((resolve) => {
        let para = document.createElement("p");
        if (type === "self") {
            para.classList.add("p-3", "bg-gray-300","dark:bg-gray-700","font-semibold");
        } else if (type === "response") {
            para.classList.add("p-3", "select-text");
        } else if (type === "error") {
            para.classList.add(
                "p-2",
                "bg-red-400",
                "text-black",
                "dark:bg-red-700",
                "dark:text-white",
                "text-center"
            );
        }

        if (type === "response") {
            continer_texts.append(para);
            let i = 0;
            let printChar = setInterval(() => {
                if (i >= text.length) {
                    clearInterval(printChar);
                    resolve();
                } else {
                    let char = text[i];
                    para.innerHTML += char;
                    i++;
                    para.scrollIntoView({ behavior: 'smooth' });
                }
            }, 10);
        } else {
            continer_texts.append(para);
            para.innerHTML = text;
            para.scrollIntoView({ behavior: 'smooth' });
            resolve();
        }
    });
}