function requestOnMain() {
          $.ajax({
          url: "/main/charts/",
          type: "GET",
          dataType: 'json',
          success: function(data){
              $("#container").empty();
              hightchartsData(data.count)
          },
          error: function(data){
             console.log('Ошибка');
          }});}


function onChangeDropDown() {
    $('#chartValues').change(function () {
        $.ajax({
          url: "/main/charts/",
          type: "GET",
          data:"region=" + this.value,
          dataType: 'json',
          success: function(data){
              $("#container").empty();
              hightchartsData(data.series_chart)
          },
          error: function(data){
             console.log('Ошибка');
          }});
    })
}

