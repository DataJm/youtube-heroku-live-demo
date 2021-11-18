console.log("Hola javascript")

d3.json("/api_views").then(data=>{

    let views_data = [
        {
          x: data.map(d=>d.channel_title),
          y: data.map(d=>d.views),
          type: 'bar'
        }
      ];
      
    Plotly.newPlot('views', views_data);

})

d3.json("/api_likes").then(data=>{
    let views_data = [
        {
          x: data.map(d=>d.channel_title),
          y: data.map(d=>d.likes),
          type: 'bar'
        }
      ];
      
    Plotly.newPlot('likes', views_data);
})