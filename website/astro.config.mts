import Compress from "astro-compress"
import { defineConfig } from 'astro/config'


export default defineConfig(
    {
        site: 'https://kekse.pages.dev',
        integrations: [
            Compress()
        ],
        redirects: {
            '/404': '/'
        }
    }
)