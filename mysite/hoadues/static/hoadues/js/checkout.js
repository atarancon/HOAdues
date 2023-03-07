// This is a public sample test API key.
// Don’t submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
const stripe = Stripe("pk_test_51MgxbRDasDOaJtxcqwlT5Hpeo1eFQXqlU8DRRTjrV7mYA26spdGiRyQRL5VRRAmpUgeWzEdpbYS7s0VXEd2yIXfd00qNzP8GwR");

// The items the customer wants to buy
//const items = [{ id: "xl-tshirt" }];

//let elements;

////initialize();
//checkStatus();

/*document
  .querySelector("#payment-form")
  .addEventListener("submit", handleSubmit);
*/

const options={
  clientSecret: '{{CLIENT_SECRET}}' ,
  //fully customizable with appearance
  appearance: {
            theme: 'stripe',
            labels: 'floating',

          }
};


//const elements = stripe.elements(options)


//create elemtn

var elements = stripe.elements();

var style = {
  base: {
    color: "#32325d",
}
};


var card = elements.create("card", { style: style});
card.mount("#card-element");

//create and mount payment Element
//const paymentElement = elements.create('payment')
//paymentElement.mount('#payment-element');



var form = document.getElementById('payment-form');

form.addEventListener( 'submit', function(ev) {
  ev.preventDefault();
  //IF the client
  //on the <form>

  stripe.confirmCardPayment( form.dataset.secret, {
    payment_method:{
      card: card,
      billing_details: {
        name: 'Jenny Rosen'
      }
    }
  }).then(function(result) {
    if (result.error) {
      console.log(result.error.message);
    } else {
      if ( result.paymentIntent.status === "succeeded"){
        console.log("Successsss !!!!!!!!!!!!!!!")

        var form = document.getElementById('payment-form');
        form.submit();

      }
    }
  });

});




//const form = document.getElementById('payment-form');
/*
form.addEventListener('submit', async (event) => {
  event.preventDefault();
*/
//const result = await stripe.createPaymentMethod({
  //type:'card',
  //card: paymentElement,
  //billing_details:{
  //  name: 'Jensen Rosen',
  //}

//});



//})




/*
  const {error} = await stripe.confirmPayment ({
    elements,
    confirmParams:{
      return_url: "https://example.com/order/123/complete"
    },

  });
*/


/*
if (error){
  const  messageContainer = document.querySelector("#error-message");
  messageContainer.textContent= error.message;
} else{console.log("Hello")}
});

*/
//let emailAddress = '';
// Fetches a payment intent and captures the client secret
/*async function initialize() {
  const response = await fetch("/create-payment-intent", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items }),
  });
  const { clientSecret } = await response.json();

  const appearance = {
    theme: 'stripe',
  };
*/
  /*elements = stripe.elements({ appearance, clientSecret });*/

  /*const linkAuthenticationElement = elements.create("linkAuthentication");*/
  /*linkAuthenticationElement.mount("#link-authentication-element"); */

  /*linkAuthenticationElement.on('change', (event) => {
    emailAddress = event.value.email;
  });
 */
  /*const paymentElementOptions = {
    layout: "tabs",
  };

  const paymentElement = elements.create("payment", paymentElementOptions);
  paymentElement.mount("#payment-element");
}
*/



/*
async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);

  const { error } = await stripe.confirmPayment({
    elements,
    confirmParams: {
      // Make sure to change this to your payment completion page
      return_url: "http://localhost:8000/checkout.html",
      receipt_email: emailAddress,
    },
  });

  // This point will only be reached if there is an immediate error when
  // confirming the payment. Otherwise, your customer will be redirected to
  // your `return_url`. For some payment methods like iDEAL, your customer will
  // be redirected to an intermediate site first to authorize the payment, then
  // redirected to the `return_url`.
  if (error.type === "card_error" || error.type === "validation_error") {
    showMessage(error.message);
  } else {
    showMessage("An unexpected error occurred.");
  }

  setLoading(false);
}

// Fetches the payment intent status after payment submission
async function checkStatus() {
  const clientSecret = new URLSearchParams(window.location.search).get(
    "payment_intent_client_secret"
  );

  if (!clientSecret) {
    return;
  }

  const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

  switch (paymentIntent.status) {
    case "succeeded":
      showMessage("Payment succeeded!");
      break;
    case "processing":
      showMessage("Your payment is processing.");
      break;
    case "requires_payment_method":
      showMessage("Your payment was not successful, please try again.");
      break;
    default:
      showMessage("Something went wrong.");
      break;
  }
}

// ------- UI helpers -------

function showMessage(messageText) {
  const messageContainer = document.querySelector("#payment-message");

  messageContainer.classList.remove("hidden");
  messageContainer.textContent = messageText;

  setTimeout(function () {
    messageContainer.classList.add("hidden");
    messageText.textContent = "";
  }, 4000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("#submit").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("#submit").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}

*/
