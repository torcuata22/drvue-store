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

        <ProductBox 
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product"
        />
        
        </div>
    </div>
 
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
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
