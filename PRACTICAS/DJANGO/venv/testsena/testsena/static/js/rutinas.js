function Migas(a){
    let x='&nbsp;&nbsp;<b><i class="fa fa-bars"></i>';
      document.write(x);
      x="";
    a.forEach(function(word){
      let b=word.split('|');
      if(b[1]!=""){
      x='&nbsp;&#171;<a href="'+b[1]+'">'+b[0]+'</a>&#187;&nbsp;';
      document.write(x);
      x="";
      }else
      {
        x='&nbsp;'+b[0]+'&nbsp;';
      document.write(x);
      }
      
    });
  }
