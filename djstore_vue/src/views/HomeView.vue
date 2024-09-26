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

      <div
        class="column is-3"
        v-for="product in latestProducts"
        :key="product.id"
      >
        <div class="box">
          <figure class="image mb-4 image-size">
            <img :src="product.get_thumbnail" alt="Product Thumbnail" />
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-grey-text">${{ product.price }}</p>
          <router-link :to="product.get_absolute_url" class="button is-dark mt-4">
            View details
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()
    document.title ='Home | Crook and Needle';
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axios
      .get('api/v1/latest-products') //removed http://localhost:8000/
      .then(response => {
        this.latestProducts = response.data
      })
        
       .catch (error =>{
        console.error('Failed to fetch latest products:', error)
      })
      this.$store.commit('setIsLoading', false)
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

.image-size {
  height: 250px;
  width: 250px;
  display:block;
  margin:auto;
}
</style>
