//https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
function Ir(que){
  location.href=que;
}
function Borra(titu,afirma,niega){


let a='<center><div class="modal-content" style="width:50%;"><p><b>Desea borrar el registro?<b></br><button onclick=\'Ir("'+afirma+'")\' class="btn btn-outline-primary w3-round-large small">Aceptar</button>&nbsp;<button onclick=\'Ir("'+niega+'")\' class="btn btn-outline-danger w3-round-large small">Cancelar</button><p></div></div></center>';
document.write(a);
}

function Confirma(titu,afirma,niega){
    if(confirm(titu)==true)
      location.href=afirma;
      else
      location.href=niega;
    }

    function Migas(a){
      let x='<p>&nbsp;&nbsp;<b><i class="fa fa-bars"></i>';
        document.write(x);
        //x="";
      a.forEach(function(word){
        let b=word.split('|');
        if(b[1]!=""){
        x='&nbsp;&#171;<a style="text-decoration:none;" href="'+b[1]+'">'+b[0]+'</a>&#187;&nbsp;';
        document.write(x);
        x="";
        }else
        {
          x='&nbsp;'+b[0]+'&nbsp;</p>';
        document.write(x);
        }
        
      });
    }
  