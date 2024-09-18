<template>
  <div class="home">
      <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
          <p class="title mb-6">
            Welcome to Crook and Needle
          </p>
          <p class="subtitle">
            The best online store for fiber artists
          </p>
        </div>
      </section>

      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <div class="column is-3"
      v-for="product in latestProducts" 
      v-bind:key="product.id"
      >
        <div class="box">
          <figure class="image mb-4"> 
            <img v-bind:src="product.get_thumbnail">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-grey-text">${{ product.price }}</p>
          View Details
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
export default {
  name: 'Home',
  data() {
   return{
     latestProducts: []
    };
  },
  components: {
    
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      axios
        .get('http://localhost:8000/api/v1/latest-products') //did not fix anything
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
//TODO: CORS issues: If the API endpoint is hosted on a different domain or port than your Vue application, you might be running into CORS (Cross-Origin Resource Sharing) issues. Check if the API endpoint is configured to allow requests from your Vue application's origin.
//TODO: Request headers or data: Inspect the request headers and data being sent from your Vue application to ensure they match what is expected by the API endpoint.
