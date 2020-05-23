      const status = document.getElementById('status');
      const output = document.getElementById('output');
      if (window.FileList && window.File && window.FileReader) {
        document.getElementById('file-selector').addEventListener('change', event => {
          output.src = '';

          const file = event.target.files[0];

          const reader = new FileReader();
          reader.addEventListener('load', event => {
            output.src = event.target.result;
          });
          reader.readAsDataURL(file);
        });
      }


