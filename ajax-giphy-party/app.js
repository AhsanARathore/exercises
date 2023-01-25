console.log("Let's get this party started!");

const $gif = $("#gif");
const $searchInput = $("#search");

function addGif(results) {
  let numResults = results.data.length;
  if (numResults) {
    let random = Math.floor(Math.random() * numResults);
    let $newdiv = $("<div>");
    let $newGif = $("<img>", {
      src: results.data[random].images.original.url,
    });
    $newdiv.append($newGif);
    $gif.append($newdiv);
  }
}

$("form").on("submit", async function (event) {
  event.preventDefault();

  const response = await axios.get("http://api.giphy.com/v1/gifs/search", {
    params: {
      q: $searchInput.val(),
      api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym",
    },
  });
  addGif(response.data);
});

$("#remove").on("click", function () {
  $gif.empty();
});
