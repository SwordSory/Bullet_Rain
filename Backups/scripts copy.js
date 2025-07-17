document.getElementById('insultForm').addEventListener('submit', displayGali);

async function displayGali(event) {
  event.preventDefault();
  console.log("Submit clicked");

  const name = document.getElementById('name').value;
  const reason = document.getElementById('reason').value;
  const output = document.getElementById('gali_output');

  console.log("Name:", name, "Reason:", reason);

  try {
    const response = await fetch('http://localhost:3000/get-insult', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, reason })
    });
    console.log("Fetch sent");

    const data = await response.json();
    console.log("Response data:", data);

    output.innerText = data.insult;
  } catch (error) {
    console.error('Fetch error:', error);
    output.innerText = 'Failed to get insult.';
  }
}



document.addEventListener("DOMContentLoaded", function () {
    const reasonBox = document.getElementById("reason");

    reasonBox.addEventListener("input", function () {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    });

    // Trigger initial height
    reasonBox.dispatchEvent(new Event("input"));
});




function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}