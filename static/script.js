document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById('fileInput');

    fileInput.addEventListener('change', function() {
    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.onload = function() {
        document.getElementById('result').innerHTML = "File submitted, please wait…"
        document.getElementById('result').style.border = "0.15em solid crimson";
        const fileContent = reader.result;
        const stringArray = fileContent.split(/[.!?]/);
        const filteredArray = stringArray.filter((str) => str.trim() !== '');
        const truncatedFile = truncateArr(filteredArray, 500);
        const theFile = { submittedArray: truncatedFile};
        
        fetch('/classify', {
            method: 'POST',
            body: JSON.stringify(theFile),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.text())
        .then(data => { 
            let theArray = JSON.parse(data)

            let confidence1, confidence2, confidenceColor1, confidenceColor2, genre1, genre2;
            confidence1 = theArray[0][1].toFixed(2);
            confidence2 = theArray[1][1].toFixed(2);
            genre1 = theArray[0][0];
            genre2 = theArray[1][0];
            if (confidence1 > 0.75) {
                confidenceColor1 = "darkgreen"; 
            }
            else {
                confidenceColor1 = "darkgoldenrod"; 
            }
            if (confidence2 > 0.5) {
                confidenceColor2 = "darkgoldenrod"; 
            }
            else {
                confidenceColor2 = "crimson"; 
            }

            document.getElementById('result').innerHTML = "<p><span style='font-weight:800;color:" + confidenceColor1 + ";font-variant:small-caps;font-size:1.2em'>" + genre1 + "</span><br>Confidence: <span style='color:" + confidenceColor1 + "'>" + confidence1 + "</span><br><br><span style='font-weight:600;color:" + confidenceColor2 + ";font-variant:small-caps;font-size:1.05em'>" + genre2 + "</span><br>Confidence: <span style='color:" + confidenceColor2 + "'>" + confidence2 + "</span></p>";
            document.getElementById('result').style.border = "0.15em solid darkgreen";
        })
        .catch(error => {
            console.error(error);
            document.getElementById('result').innerHTML = "Something went wrong. Are you sure the file is a .txt file with UTF-8 encoding?"
        });
    };
    reader.readAsText(file);

    });

  
    function truncateArr(arr, maxLength) {
        if (arr.length > maxLength) {
            const steps = (arr.length-1) / (maxLength-1);
            let marks=[];
            for(let i=0; i<maxLength; i++){
                marks.push(arr[Math.round(i*steps)]);
            }
            return marks;
        }
        else {
            return arr;
        }
    }
});

