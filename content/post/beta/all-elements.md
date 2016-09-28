+++
title = "All elements: a test for all layout elements"
draft = true
date = "2016-09-28T09:55:24+02:00"
tags = ["beta"]
banner = "https://farm2.staticflickr.com/1501/26687024535_eda95a3ea5_h_d.jpg"
+++

This page shows how all possible elements work on a page<!--more-->

<hr />
# "Meta"

The title is displayed like this when you set `banner = <src>` in front matter

The "Meta" section displays:

- Table of Contents
- Published date
- Modified date (if provided)
- Tags. Set `tags = ["tag1", "tag2", ...]` to display tags.
- Word count and reading time

<hr />

# Typography

## Subheading (H2)
## Sub-subheading (H3)

The first paragraph after a heading displays a drop cap.

Subsequent paragraphs are indented.

Further subheadings (H4-H6) will have the same size as H3.

- This
- Is
	- An
	- Unordered
		- List

1. This
2. Is
	3. An
	4. Ordered
		5. List

This is [a link](/).

<hr />

# Images

There are several types of images:

- image
- fullimage
- gallery
- inlineimage

## Image

Display a single image as a block element with possible description.

```
{{</* image src author? description? link? >}text?{ {</ image */>}}
```


param | type |   |description
------|------|----------|-------------
src | String | required | source of the image
author | String | optional | 
description | String | optional |
link | String | optional | link to the page where the image is displayed, or to a larger version of the image
text | any | optional | If you want to display larger texts, or markdown texts, or other shortcodes in image description

### Example

```
{{%/* image src="https://farm4.staticflickr.com/3729/12516648584_b8aa06a5da_k_d.jpg" author="jason jenkins" description="Time Passes By the Wise Old Oak" link="https://www.flickr.com/photos/jdub1980/12516648584/in/photolist-k546xW-jzs7yy-c2JdAj-wcvM7R-nWLqdL-os1Njy-EecbfS-CGA2pX-dSryYh-oX5gy3-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-7KaLhV-anQAgj-jwVoha-qoo2eQ-nB4fzi-5YYY4B-5XmMo3-84Ymu5-qrwmZC-nQb1F3-7MDFF6-oXdto8-5MkJe6-7KeF1y-7Gc6C3-gPfsQh-qtW1Ka-rBRz1n-89yQE5-oZsYyb-EoaxPD-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-dRUwmA-bxNrWT-5YYYcp-dfYTGj-jwYMs3-pCz4ai-ikS2op-nMsPhh-oEZELN" %}}[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/){{%/ image */%}}

```

{{% image src="https://farm4.staticflickr.com/3729/12516648584_b8aa06a5da_k_d.jpg" author="jason jenkins" description="Time Passes By the Wise Old Oak" link="https://www.flickr.com/photos/jdub1980/12516648584/in/photolist-k546xW-jzs7yy-c2JdAj-wcvM7R-nWLqdL-os1Njy-EecbfS-CGA2pX-dSryYh-oX5gy3-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-7KaLhV-anQAgj-jwVoha-qoo2eQ-nB4fzi-5YYY4B-5XmMo3-84Ymu5-qrwmZC-nQb1F3-7MDFF6-oXdto8-5MkJe6-7KeF1y-7Gc6C3-gPfsQh-qtW1Ka-rBRz1n-89yQE5-oZsYyb-EoaxPD-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-dRUwmA-bxNrWT-5YYYcp-dfYTGj-jwYMs3-pCz4ai-ikS2op-nMsPhh-oEZELN" %}}[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/){{%/ image %}}

## Fullimage

Display a single image as a block element that stretches to the full width of the page

```
{{</* fullimage src author? description? link? */>}}
```


param | type |   |description
------|------|----------|-------------
src | String | required | source of the image
author | String | optional | 
description | String | optional |
link | String | optional | link to the page where the image is displayed, or to a larger version of the image

### Example

```
{{</* fullimage src="https://farm8.staticflickr.com/7103/7239478006_eb31be8f6b_h_d.jpg" author="jimnista" description="Sunset Beach Eclipse May 20th 2012. CC BY 2.0" link="https://www.flickr.com/photos/jimnista/7239478006/in/photolist-c2JdAj-5YYY4B-nWLqdL-os1Njy-EecbfS-CGA2pX-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-anQAgj-qoo2eQ-nB4fzi-84Ymu5-nQb1F3-7MDFF6-5MkJe6-gPfsQh-qtW1Ka-rBRz1n-89yQE5-EoaxPD-dfYTGj-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-pCz4ai-ikS2op-bjoHsB-7GkTyc-eELrma-DXpLCD-9dXKU2-dUob1f-pbB4Yd-FqBh7j-e29hm5-DQEXpX-6anRyo-qeLt3h-6oP59C-6aiH9V-2sSsq9-fUsMZw-63hSwT-9Gn8DP-nfRyBD" */>}}
```

{{< fullimage src="https://farm8.staticflickr.com/7103/7239478006_eb31be8f6b_h_d.jpg" author="jimnista" description="Sunset Beach Eclipse May 20th 2012. CC BY 2.0" link="https://www.flickr.com/photos/jimnista/7239478006/in/photolist-c2JdAj-5YYY4B-nWLqdL-os1Njy-EecbfS-CGA2pX-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-anQAgj-qoo2eQ-nB4fzi-84Ymu5-nQb1F3-7MDFF6-5MkJe6-gPfsQh-qtW1Ka-rBRz1n-89yQE5-EoaxPD-dfYTGj-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-pCz4ai-ikS2op-bjoHsB-7GkTyc-eELrma-DXpLCD-9dXKU2-dUob1f-pbB4Yd-FqBh7j-e29hm5-DQEXpX-6anRyo-qeLt3h-6oP59C-6aiH9V-2sSsq9-fUsMZw-63hSwT-9Gn8DP-nfRyBD" >}}

## Gallery

Display a collection of images

```
{{</* gallery >}}items?{ {</ gallery */>}}
```


param | type |   |description
------|------|----------|-------------
items | any | optional | anything, really. However, it's assumed you will use `{ {< image >}}`s (see above).

### Example

```
{{</* gallery >}}

{{% image src="https://farm4.staticflickr.com/3729/12516648584_b8aa06a5da_k_d.jpg" author="jason jenkins" description="Time Passes By the Wise Old Oak" link="https://www.flickr.com/photos/jdub1980/12516648584/in/photolist-k546xW-jzs7yy-c2JdAj-wcvM7R-nWLqdL-os1Njy-EecbfS-CGA2pX-dSryYh-oX5gy3-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-7KaLhV-anQAgj-jwVoha-qoo2eQ-nB4fzi-5YYY4B-5XmMo3-84Ymu5-qrwmZC-nQb1F3-7MDFF6-oXdto8-5MkJe6-7KeF1y-7Gc6C3-gPfsQh-qtW1Ka-rBRz1n-89yQE5-oZsYyb-EoaxPD-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-dRUwmA-bxNrWT-5YYYcp-dfYTGj-jwYMs3-pCz4ai-ikS2op-nMsPhh-oEZELN" %}}[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/){{%/ image %}}

{{< image src="https://farm8.staticflickr.com/7103/7239478006_eb31be8f6b_h_d.jpg" author="jimnista" description="Sunset Beach Eclipse May 20th 2012. CC BY 2.0" link="https://www.flickr.com/photos/jimnista/7239478006/in/photolist-c2JdAj-5YYY4B-nWLqdL-os1Njy-EecbfS-CGA2pX-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-anQAgj-qoo2eQ-nB4fzi-84Ymu5-nQb1F3-7MDFF6-5MkJe6-gPfsQh-qtW1Ka-rBRz1n-89yQE5-EoaxPD-dfYTGj-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-pCz4ai-ikS2op-bjoHsB-7GkTyc-eELrma-DXpLCD-9dXKU2-dUob1f-pbB4Yd-FqBh7j-e29hm5-DQEXpX-6anRyo-qeLt3h-6oP59C-6aiH9V-2sSsq9-fUsMZw-63hSwT-9Gn8DP-nfRyBD" />}}

{{</ gallery */>}}

```

{{< gallery >}}

{{% image src="https://farm4.staticflickr.com/3729/12516648584_b8aa06a5da_k_d.jpg" author="jason jenkins" description="Time Passes By the Wise Old Oak" link="https://www.flickr.com/photos/jdub1980/12516648584/in/photolist-k546xW-jzs7yy-c2JdAj-wcvM7R-nWLqdL-os1Njy-EecbfS-CGA2pX-dSryYh-oX5gy3-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-7KaLhV-anQAgj-jwVoha-qoo2eQ-nB4fzi-5YYY4B-5XmMo3-84Ymu5-qrwmZC-nQb1F3-7MDFF6-oXdto8-5MkJe6-7KeF1y-7Gc6C3-gPfsQh-qtW1Ka-rBRz1n-89yQE5-oZsYyb-EoaxPD-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-dRUwmA-bxNrWT-5YYYcp-dfYTGj-jwYMs3-pCz4ai-ikS2op-nMsPhh-oEZELN" %}}[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/){{%/ image %}}

{{< image src="https://farm8.staticflickr.com/7103/7239478006_eb31be8f6b_h_d.jpg" author="jimnista" description="Sunset Beach Eclipse May 20th 2012. CC BY 2.0" link="https://www.flickr.com/photos/jimnista/7239478006/in/photolist-c2JdAj-5YYY4B-nWLqdL-os1Njy-EecbfS-CGA2pX-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-anQAgj-qoo2eQ-nB4fzi-84Ymu5-nQb1F3-7MDFF6-5MkJe6-gPfsQh-qtW1Ka-rBRz1n-89yQE5-EoaxPD-dfYTGj-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-pCz4ai-ikS2op-bjoHsB-7GkTyc-eELrma-DXpLCD-9dXKU2-dUob1f-pbB4Yd-FqBh7j-e29hm5-DQEXpX-6anRyo-qeLt3h-6oP59C-6aiH9V-2sSsq9-fUsMZw-63hSwT-9Gn8DP-nfRyBD" />}}

{{</ gallery >}}

## Inlinemage

Display a single image inline. It will appear on the left side of the surrounding text block. Currently only usable inside `{{</* quote */>}}`

```
{{</* quote >}}
{{< inlineimage src author? description? link? >}text?{ {</ image >}}
{{</ quote */>}}
```


param | type |   |description
------|------|----------|-------------
src | String | required | source of the image
author | String | optional | 
description | String | optional |
link | String | optional | link to the page where the image is displayed, or to a larger version of the image
text | any | optional | If you want to display larger texts, or markdown texts, or other shortcodes in image description

### Example

```
{{%/* quote %}}

{{% inlineimage src="https://farm4.staticflickr.com/3729/12516648584_b8aa06a5da_k_d.jpg" author="jason jenkins" description="Time Passes By the Wise Old Oak" link="https://www.flickr.com/photos/jdub1980/12516648584/in/photolist-k546xW-jzs7yy-c2JdAj-wcvM7R-nWLqdL-os1Njy-EecbfS-CGA2pX-dSryYh-oX5gy3-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-7KaLhV-anQAgj-jwVoha-qoo2eQ-nB4fzi-5YYY4B-5XmMo3-84Ymu5-qrwmZC-nQb1F3-7MDFF6-oXdto8-5MkJe6-7KeF1y-7Gc6C3-gPfsQh-qtW1Ka-rBRz1n-89yQE5-oZsYyb-EoaxPD-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-dRUwmA-bxNrWT-5YYYcp-dfYTGj-jwYMs3-pCz4ai-ikS2op-nMsPhh-oEZELN" %}}[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/){{%/ image %}}  some text some other text

{{%/ quote */%}}

```

{{% quote %}}

{{% inlineimage src="https://farm4.staticflickr.com/3729/12516648584_b8aa06a5da_k_d.jpg" author="jason jenkins" description="Time Passes By the Wise Old Oak" link="https://www.flickr.com/photos/jdub1980/12516648584/in/photolist-k546xW-jzs7yy-c2JdAj-wcvM7R-nWLqdL-os1Njy-EecbfS-CGA2pX-dSryYh-oX5gy3-qcWMHh-8QR93e-HRUzeG-EeGxU4-dTNdV9-7KaLhV-anQAgj-jwVoha-qoo2eQ-nB4fzi-5YYY4B-5XmMo3-84Ymu5-qrwmZC-nQb1F3-7MDFF6-oXdto8-5MkJe6-7KeF1y-7Gc6C3-gPfsQh-qtW1Ka-rBRz1n-89yQE5-oZsYyb-EoaxPD-qGDLgw-7dsADr-8KbVbG-niaoB2-io7x6S-dRUwmA-bxNrWT-5YYYcp-dfYTGj-jwYMs3-pCz4ai-ikS2op-nMsPhh-oEZELN" %}}[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/){{%/ image %}}  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ut aliquam ex. In nunc ipsum, molestie hendrerit ultricies a, finibus gravida lectus. Aenean a eros mauris. Donec non ornare est. Donec tincidunt posuere risus et ultrices. Vivamus volutpat dui a commodo fringilla. Aliquam ultricies nec risus id rhoncus. Sed tempus hendrerit dui placerat pharetra. Etiam maximus mi eu venenatis pretium. Quisque faucibus mi in elit dictum, vitae scelerisque purus sodales. Donec lobortis lorem ut turpis dignissim, quis molestie odio ultrices. In sit amet varius nunc.

Aliquam posuere aliquet tristique. Donec eu ligula sit amet purus convallis porttitor. Morbi a porta enim, quis rutrum turpis. In suscipit diam auctor nisi vehicula, ac dignissim libero interdum. Nam fringilla eros nec ultrices mattis. Curabitur malesuada metus vitae arcu condimentum, sit amet tempus orci porttitor. Sed consectetur scelerisque odio convallis rutrum. Curabitur auctor a elit gravida hendrerit. Duis id lacinia sapien. Nulla consectetur consequat congue. Pellentesque gravida ac lacus a iaculis. Sed at purus ipsum.

{{%/ quote %}}

<hr />

# Quotes

A page-wide element displaying the quote and the author

```
{{%/* quote author? link? %}}text?{{%/ quote */%}}
```


param | type |   |description
------|------|----------|-------------
author | String | optional | 
link | String | optional | 
text | String | optional | 

## Example

```
{{%/* quote author="Hugo Website" link="https://gohugo.io" %}}
*Make the Web Fun Again*

Introducing Hugo, a new idea around making website creation simple again. Hugo flexibly works with many formats and is ideal for blogs, docs, portfolios and much more. Hugo’s speed fosters creativity and makes building a website fun again.
{{%/ quote */%}}
```

{{% quote author="Hugo Website" link="https://gohugo.io" %}}
*Make the Web Fun Again*

Introducing Hugo, a new idea around making website creation simple again. Hugo flexibly works with many formats and is ideal for blogs, docs, portfolios and much more. Hugo’s speed fosters creativity and makes building a website fun again.
{{%/ quote %}}

<hr />

# Video

A responsive video block. Currently only supports youtube

```
{{</* video id? */>}}
```

param | type |   |description
------|------|----------|-------------
id | youtube | required | 

## Example

```
{{</* video youtube="w7Ft2ymGmfc" */>}}
```

{{< video youtube="w7Ft2ymGmfc" >}}

<hr />
# Code blocks

## Inline

Just use \`backticks\`. 

### Example

```
This is some inline `code` in a text
```

This is some inline `code` in a text

## Block

Use "fenced code blocks" with optional language name. It will be rendered as a full width block with a [zenburn](https://github.com/richleland/pygments-css/blob/master/zenburn.css) theme.

### Example

<pre><code>
```python
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill
```
</code></pre>

```python
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill
```

<hr />

# Banner

If the page has `banber = <src>` set in its front matter, it will display the page title like you see on this very page. To replicate the same behaviour elsewhere in text use the banner shortcode:

```
{{</* banner src title */>}}
```

param | type |   |description
------|------|----------|-------------
src | String | required | 
title | String | required | 


## Example

```
{{</* banner src="https://farm2.staticflickr.com/1501/26687024535_eda95a3ea5_h_d.jpg" title="A title" */>}}
```

{{< banner src="https://farm2.staticflickr.com/1501/26687024535_eda95a3ea5_h_d.jpg" title="A title" >}}

<hr />
# Acknowledgements

- Banner: [Lenny K Photography](https://www.flickr.com/photos/lennykphotography/26687024535/in/photolist-GEeYCF-EDGjje-aUkoTr-aA877L-njnKGG-dL6s9y-eELrma-9pnw9W-pbB4Yd-r2LrMM-6QJrA-6BUCg4-pBQqjU-ee4JUU-spYj9t-GUXE34-EYQtw3-rgTDFq-daQ88F-dkLsdU-DbTK2A-oW9wQS-dfgj4V-e5afKu-cLGK41-LFKPG-aGe9AF-u5cG3W-nw1Txo-r2EenQ-eit4dZ-mHw3pr-jfRaEa-oWayq3-oYz2jo-kAaymz-6EaXLF-ptuKpG-ebaWZ8-6BGXw7-dFivdE-f9PKqh-b3ijNH-dgmMmr-iVvhHy-5UGaAt-9B4CZ1-q1RNBa-5TWCYe-gwmN7H) [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)
