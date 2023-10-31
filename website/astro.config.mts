import sitemap from "@astrojs/sitemap"
import robotsTxt from "astro-robots-txt"

import { defineConfig } from 'astro/config'


export default defineConfig(
    {
        site: 'https://kekse.pages.dev',
        build: {
            assets: 'assets/bundle'
        },
        integrations: [
            sitemap({
                lastmod: new Date()
              }),
            robotsTxt()
        ]
    }
)