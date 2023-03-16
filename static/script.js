function classifyText() {
  document.getElementById('result').innerHTML = "File submitted, please wait…"
  document.getElementById('result').style.border = "0.15em solid crimson";
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  fetch('/classify', {
	method: 'POST',
	body: file
  })
  .then(response => response.text())
  .then(data => { 
    let genre = JSON.parse(data).genres; 
    let sentiment = JSON.parse(data).sentiments; 
    document.getElementById('result').innerHTML = "Genre: <span style='font-weight:800;color:cornflowerblue;font-variant:small-caps;font-size:1.2em'>" + genre + "</span>";
    document.getElementById('result').style.border = "0.15em solid darkgreen";
  })
  .catch(error => {
      console.error(error);
      document.getElementById('result').innerHTML = "Something went wrong. Are you sure the file is a .txt file with UTF-8 encoding?"
  });
}

