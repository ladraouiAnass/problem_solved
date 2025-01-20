async function processJson() {
  const fileInput = document.getElementById('jsonFile');
  const calculateButton = document.getElementById('calculateButton');
  const errorMessage = document.getElementById('error-message');
  const percentageText = document.getElementById('percentage');
  const progressCircle = document.querySelector('.progress-circle');
  const loadingSpinner = document.getElementById('loadingSpinner');

  errorMessage.textContent = '';

  if (!fileInput.files.length) {
    errorMessage.textContent = 'Please upload a JSON file.';
    return;
  }


  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = async function (event) {
    try {
      const jsonData = JSON.parse(event.target.result); 
      const response = await fetch('/calculate-percentage/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', 
        },
        body: JSON.stringify(jsonData), 
      });

      if (!response.ok) {
        throw new Error(`Failed to fetch data from the server. Status: ${response.status}`);
      }

      const result = await response.json();

      if (typeof result.number !== 'number' || result.number < 0 || result.number > 100) {
        errorMessage.textContent = 'The server did not return a valid number (0-100).';
        return;
      }

      const percentage = result.number;
      percentageText.textContent = `${percentage}%`;
      progressCircle.style.setProperty('--percentage', `${percentage}%`);
    } catch (e) {
      errorMessage.textContent = `Error: ${e.message}`;
    } 
  };

  reader.readAsText(file); 
}
