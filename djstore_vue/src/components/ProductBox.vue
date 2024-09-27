<template>
    <div class="column is-3">
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
</template>    

<script>
    export default {
        name: 'ProductBox',
        props: {
            product: Object
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