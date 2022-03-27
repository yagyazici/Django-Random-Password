let slider = document.querySelector("#id_length");
let p = document.querySelector("#value");
p.innerHTML = `Length: ${slider.value}`;
slider.oninput = function () {
  p.innerHTML = `Length: ${this.value}`;
};

function checkForm() {
  let checkboxes = document.querySelectorAll(".form-check");
  let allchecked = false;
  checkboxes.forEach(element => {
    if (element.checked == true){
      allchecked = true;
      return;
    }
  });
  allchecked == false ? alert("You have to check at least one") : "";
}

let button = document.querySelector("#create");
button.addEventListener("click", checkForm);

function copyPassword() {
  let password = document.querySelector("#password");
  navigator.clipboard.writeText(password.innerHTML);
  alert("Copied to clipboard")
}

if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}