<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is_12">
                    <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>
            <div
                class="column is-3"
                v-for="product in category.products"
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
    import { toast } from 'bulma-toast'


    export default{
        name:'Category',
        data() {
            return {
                category: {
                    products: [],
                }
            }
        },
        mounted() {
            this.getCategory()
        },
        watch: {
            '$route.params.category_slug': 'getCategory'
        },
        methods: {
            async getCategory() {
                const category_slug = this.$route.params.category_slug;
                this.$store.commit('setIsLoading', true);
                console.log('category_slug:', category_slug);
            try {
                const response = await axios.get(`/api/v1/products/${category_slug}`);
                this.category = response.data; // has category and product
            } catch (error) {
                console.log('Error fetching category:', error);
                toast({
                    message: 'Something went wrong. Please try again.',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                });
            } finally {
                this.$store.commit('setIsLoading', false);
                }
    }
  }
}



</script>