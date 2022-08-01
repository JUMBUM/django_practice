function doSomething(){           
    a = document.getElementById('inputA').value;
    b = document.getElementById('inputB').value;

    document.getElementById('valueA').innerHTML = a;
    document.getElementById('valueB').innerHTML = b;
    document.getElementById('valueC').innerHTML = Number(a) + Number(b);
    }

    function getTime(){
        alert(new Date())
    }