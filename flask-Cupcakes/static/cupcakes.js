function unjsonify(cupcake) {
  return `
    <div data-id=${cupcake.id} class="div">
    <li> ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating} 
     <img class="Cupcake-img"
    style= "max-width: 200px; max-height: 200px; align-self: center"
    src="${cupcake.image}"
    >
    <button class="delete-button" data-id=${cupcake.id}>Remove</button>
    </li>
    </div>
    `;
}

async function showCupcakes() {
  const response = await axios.get(`/api/cupcakes`);

  for (let cupcake of response.data.cupcakes) {
    let newcupcake = $(unjsonify(cupcake));
    $("#cupcakes-list").append(newcupcake);
  }
}

$("#new-cupcake").on("submit", async function (event) {
  event.preventDefault();

  let flavor = $("#form-flavor").val();
  let rating = $("#form-rating").val();
  let size = $("#form-size").val();
  let image = $("#form-image").val();

  const responseNewCupcake = await axios.post(`/api/cupcakes`, {
    flavor,
    rating,
    size,
    image,
  });

  let newcupcake = $(unjsonify(responseNewCupcake.data.cupcake));
  $("#cupcakes-list").append(newcupcake);
  $("new-cupcake").trigger("reset");
});

async function deletecupcake(event) {
  event.preventDefault();
  $(this).closest(".div").remove();
}

$(".delete-button").click(deletecupcake);

$(showCupcakes);
