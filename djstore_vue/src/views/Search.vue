<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="columns is-12">
                <!-- <h1 class="title is-size-2"> Search Results</h1> -->
                <br><br>
                <div class="columns is-narrow is-12">
                    <h2 class="is-size-2 has-grey-text" style="margin-top:65px;">You searched for: "{{ query }}"</h2>
                </div>
            </div>


            <div class="column is-12">
            <ProductBox 
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product" />
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import ProductBox from '@/components/ProductBox'

    export default{
    name: 'Search',
    data() {
        return {
            products: [],
            query: ''
        };
    },
    mounted() {
        document.title = 'Search | Crook and Needle';
        let uri = window.location.search.substring(1);
        let params = new URLSearchParams(uri);

        if (params.get('query')) {
            this.query = params.get('query');
            this.performSearch();
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/products/search/', {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false) 
        },
        search(query) {
            this.query = query;
            this.performSearch();
        }
    },
    components: { ProductBox }
}
</script>