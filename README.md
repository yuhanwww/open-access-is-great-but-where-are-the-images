## TLDR

Museums are sharing metadata on some of their artworks as part of "[Open Access](https://en.wikipedia.org/wiki/Open_access)" programs. Unfortunately, it's not easy at all to access the related artwork image URLs.

This project makes it easy to access that image url data in either CSV or SQLite format.

## Where are the images?

- [National Gallery of Art](1.data/nga-images.csv)
- [Met - Images CSV](1.data/met-images.csv)
- [Chicago - Images CSV](1.data/chicago-images.csv)
- thanks to [@whatever](https://github.com/whatever), the same image-identifier-to-url data is also available in sqlite3 format!
  - sqlite3 file -> [open-access-is-great-but-where-are-the-images.db](2.sqlify/open-access-is-great-but-where-are-the-images.db)

## Reasons to do this (/rant/soapbox)

- the Met doesn't make image URLs part of its [frequently updated CSV dataset file](https://github.com/metmuseum/openaccess/) -- "Images are not included and are not part of the dataset"

- the Art Institute of Chicago does not make image URLs easily available either -- warning of this in the exact same language as the Met: "Images are not included and are not part of the dataset" from its otherwise well thought out [API documentation](https://github.com/art-institute-of-chicago/api-data)

- the National Gallery does not make image URLs for the exact same reason as above, "mages and media files are not included in the dataset." [The NGA API](https://github.com/NationalGalleryOfArt/opendata) is no different from the above ones. Compared to Met and the Art Institute of Chicago, the National Gallery of Art's images are more difficult to access as the image urls are not even directly available in the json files.

- does giving access to the image URLs feel reductive of the richness of this data? why are institutions putting in so much effort to publish Open Access datasets and keep them updated, but specifically hide the image URLs? what's going on? am I crazy?

- in the case of the Met, getting all the image URLs requires downloading a 300 Mb CSV file (as of Feb 2021) and making 600k API calls which take multiple hours to complete

- although CSV and JSON files are text-based and thus easy to consume on all platforms (the Met provides CSV, the Art Institute of Chicago JSON), past a certain file size or number of files, these become difficult to work with (does Excel allow importing a 300Mb CSV file?) For this reason, I am also be publishing a sqlite database containing Open Access data for both Chicago and the Met.

## TODO

- merge/include all data from openaccess (not just the image urls) in the CSV & sqlite data dumps i.e. merge metadata + urls in a single csv
- refresh data as the last time all of this data was processed was in ~2021
  - update: the Met data was updated as of May 2024
- expose a web version of the database using the sqlite-fs-http trick
