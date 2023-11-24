import sitemap from '@astrojs/sitemap'
import robotsTxt from 'astro-robots-txt'

import { defineConfig } from 'astro/config'


export default defineConfig(
    {
        site: 'https://schokokeks.pages.dev',
        integrations: [
            sitemap({
                lastmod: new Date(),
                changefreq: 'never'
              }),
            robotsTxt()
        ],
        build: {
            assets: 'assets'
        }
    }
)