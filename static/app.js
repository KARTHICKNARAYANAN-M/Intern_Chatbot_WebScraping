class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}



const chatbox = new Chatbox();
chatbox.display();


/*function onSearch()
             {
                var Branch = document.getElementsByClassName("Branch")[0];
                var branchtext = Branch.value;
                if(branchtext == "")
                {
                    alert("Please Enter the branch")
                    return;
                }
                  var GlobalData;
             fetch('http://127.0.0.1:5000/scraping', {
                    method: 'POST',
                     body: JSON.stringify({branch : branchtext}),
                     mode: 'cors',
                     headers: {
                    'Content-Type': 'application/json'
                },
            })
            .then(response => response.json())  // Parse the JSON response
            .then(data => {
                //console.log(data);
                DisplayData(data)  // Log the parsed JSON data
            })
           
          
          }
          */

          function onSearch() {
            var Branch = document.getElementsByClassName("Branch")[0];
            var branchtext = Branch.value;
            if(branchtext == "") {
                alert("Please Enter the branch");
                return;
            }
        
            var loader = document.getElementById('loader'); // Get loader element
            loader.style.display = 'block'; // Show loader
        
            fetch('http://127.0.0.1:5000/scraping', {
                method: 'POST',
                body: JSON.stringify({ branch: branchtext }),
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            .then(response => response.json())
            .then(data => {
                DisplayData(data);
                loader.style.display = 'none'; // Hide loader after data is loaded
            })
            .catch(error => {
                console.error('Error:', error);
                loader.style.display = 'none'; // Hide loader if there's an error
            });
        }
        

       /*  function DisplayData(datas)
          {
              title = datas.title;
              link = datas.link;
              img = datas.img;

              var length = Math.min(title.length, link.length, img.length);

              console.log(img.length);

              var Parent = document.getElementsByClassName("card-container")[0];

              for(var i = 0; i < length; i++)
              {
                var div = document.createElement("div");
                div.className = "card";

                var baselink = "https://www.edx.org" + link[i];

                div.innerHTML +=

                `
                    
                        <img src = ${img[i]} >
                        <h3> ${title[i]} </h3>
                        <button>
                             <a href = ${baselink} target="_blank">Course Description</a>
                         </button>
                    
                     

                `
                Parent.appendChild(div);
              } 
              
             
          }*/

          function DisplayData(datas) {
            title = datas.title;
            link = datas.link;
            img = datas.img;

            console.log(img);
        
            var length = Math.min(title.length, link.length, img.length);
        
            var Parent = document.getElementsByClassName("card-container")[0];
            
            // Clear existing content
            Parent.innerHTML = '';
        
            for(var i = 0; i < length; i++) {
                var div = document.createElement("div");
                div.className = "card";
        
                var baselink = "https://www.edx.org" + link[i];
        
                div.innerHTML +=
                `
                    <img src = ${img[i]} >
                    <h3> ${title[i]} </h3>
                    <button>
                        <a href = ${baselink} target="_blank">Course Description</a>
                    </button>
                `
                Parent.appendChild(div);
            } 
        }
        