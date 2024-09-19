<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-if="product.get_image" :src="product.get_image">
                </figure>
                <h1 class="title">{{ product.name }}</h1>
                <p>{{ product.description }}</p>
            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p><strong>Price: </strong>${{ product.price }}</p>
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" v-model="quantity">
                    </div>
                    <div class="control">
                        <a class="button is-info" @click="addToCart">Add to Cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1
        };
    },
    mounted() {
        this.getProduct();
    },
    methods: {
        getProduct() {
            const category_slug = this.$route.params.category_slug;
            const product_slug = this.$route.params.product_slug;
            console.log(`Fetching product with category_slug: ${category_slug} and product_slug: ${product_slug}`);
            axios
                .get(`/api/v1/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data;
                })
                .catch(error => {
                    console.log('Error fetching product:', error);
                });
        },
        addToCart() {
            // Implementation for adding to cart
        }
    }
};
</script>

<style scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}
</style>
