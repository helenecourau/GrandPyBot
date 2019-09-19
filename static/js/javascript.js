
function initMap(lat, lng) {
    var pElt = document.getElementById("map");
    const mq = window.matchMedia( "(max-width: 1280px)" );
    if (mq.matches) {
        pElt.style.height = "30%";
    } else {
        pElt.style.height = "100%";
    }
    
    var map = new google.maps.Map(pElt, {
                center: {lat: lat, lng: lng},
                zoom: 15
    });
    
    var marker = new google.maps.Marker({
    position: {lat: lat, lng: lng},
    title:"Localisation"
    });

    marker.setMap(map);
    var footerElt = document.querySelector("footer")
    footerElt.style.position = "relative";
    footerElt.style.width = "99%";
}

function insertWiki(title, description, url) {
    var answerElt = document.createElement("div");
    answerElt.id = "wiki"; 
    
    var titleElt = document.createElement("h3");
    titleElt.id = "title";
    titleElt.textContent = title;
    titleElt.style.textAlign = "center";

    var descriptionElt = document.createElement("p");
    descriptionElt.id = "description";
    descriptionElt.textContent = description;
    
    document.getElementById("wikiPlace").appendChild(answerElt); 
    document.getElementById("wiki").appendChild(titleElt);
    document.getElementById("wiki").appendChild(descriptionElt);
    document.getElementById("description").insertAdjacentHTML("afterEnd", 
    `<p id="url">Tu en sauras plus <a href="${url}" target="_blank">sur ce lien</a>.</p>`);
}

function insertAdress(adress) {
    var adressElt = document.createElement("p");
    adressElt.id = "adress";
    adressElt.textContent = "Voici l'adresse dont tu as besoin : " + adress + ". Je te mets une petite carte en-dessous et n'hésite pas si tu as d'autres questions !";
    document.getElementById("adressPlace").appendChild(adressElt);
}

function loader() {
    var loaderElt = document.createElement("div");
    loaderElt.id = "loaderImp";
    loaderElt.style.border = "10px solid #f3f3f3"; 
    loaderElt.style.borderTop = "10px solid #6b8686"; 
    loaderElt.style.borderRadius = "50%";
    loaderElt.style.width = "30px";
    loaderElt.style.height = "30px";
    loaderElt.style.animation = "spin 2s linear infinite";
    loaderElt.style.margin = "auto";
    document.getElementById("loader").appendChild(loaderElt);
}

function insertSentence(random_sentence) {
    var randomElt = document.createElement("p");
    randomElt.id = "random";
    randomElt.textContent = random_sentence;
    document.getElementById("sentencePlace").appendChild(randomElt);
}

function clean() {
    var pElt = document.getElementById("map");
    pElt.style.height = "0%";
    if (document.getElementById("wiki")){
        document.getElementById("wikiPlace").removeChild(document.getElementById("wiki"));
    }
    if (document.getElementById("adress")){
        document.getElementById("adressPlace").removeChild(document.getElementById("adress"));
    }
    if (document.getElementById("random")){
        document.getElementById("sentencePlace").removeChild(document.getElementById("random"));
    }
    if (document.getElementById("errorAll")){
        document.getElementById("sentencePlace").removeChild(document.getElementById("errorAll"));
    }
    if (document.getElementById("errorMap")){
        document.getElementById("sentencePlace").removeChild(document.getElementById("errorMap"));
    }
    if (document.getElementById("errorWiki")){
        document.getElementById("sentencePlace").removeChild(document.getElementById("errorMap"));
    }
}
