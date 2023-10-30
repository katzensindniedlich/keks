import { defineConfig } from 'astro/config'


export default defineConfig(
    {
        site: 'https://kekse.pages.dev',
        build: {
            assets: 'assets/bundle'
        }
    }
)
