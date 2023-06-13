$(document).ready(function() {
    var chatLog = $('#chat-log');
    var userInput = $('#user-input');
  
    function appendMessage(message, sender) {
      var className = (sender === 'bot') ? 'bot-message' : 'user-message';
      chatLog.append('<div class="' + className + '">' + message.replace(/\n/g, '<br>') + '</div>');
      chatLog.scrollTop(chatLog[0].scrollHeight);
    }
  
    function sendMessage(message) {
      appendMessage(message, 'user');
      // Make an AJAX request to your Django backend to retrieve the chatbot response
      $.ajax({
        url: '/chatbot/get_response/',
        type: 'POST',
        data: {
          message: message
        },
        success: function(response) {
          appendMessage(response.message, 'bot');
        }
      });
    }
  
    userInput.keydown(function(e) {
      if (e.which === 13) {
        var message = userInput.val().trim();
        if (message !== '') {
          userInput.val('');
          sendMessage(message);
        }
      }
    });
  
    userInput.focus();
  });
  