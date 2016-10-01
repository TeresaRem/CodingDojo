// misc notes

    <script type="text/javascript">
      $(document).ready(function(){
          $('#m').keypress(function(e){
            if(e.which == 13){
                if(e.shiftKey){
                  $('form').submit(function(){
                    socket.emit('chat message', $('#m').val());
                    $('#m').val('');
                    return false;
                  });
                }
             }
          });
      });
    </script>


    // get character

    http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_event_key_keycode