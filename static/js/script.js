    function search_table() {

        const input = document.getElementById("table-search");
        let filter = input.value.toUpperCase();
        let table = document.getElementById("myTable");
        let tr = document.querySelectorAll(".mytr");

        tr.forEach(e => {

            let result = e.getElementsByTagName('th')[1];
            if(result){
                txvalue= result.textContent || result.innerText;
                if(txvalue.toUpperCase().indexOf(filter) >-1){
                    e.style.display=""
                }else{
                    e.style.display='none'
                }
            }
        })

    }