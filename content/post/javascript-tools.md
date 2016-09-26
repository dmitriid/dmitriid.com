+++
date = "2016-09-21T13:38:57+02:00"
draft = true
title = "Javascript Tools: A Story in Disgrace"
summary = "Web developers are expected to build increasingly sophisticated UIs faster, cheaper, with tools that have not evolved with the times."
+++

Consider this quote

{{% quote author="Some Guy" %}}
Web developers are expected to build increasingly sophisticated UIs faster, cheaper, with tools that have not evolved with the times. Why is the trivial task of centering an element with CSS so obtusely complex? CSS was designed to separate presentation from content, but even with Flexbox, a trivial change in layout can require deep changes in both the HTML content and the CSS presentation. CSS layout primitives are not expressive enough - it doesn't really matter that some div is 720px wide - what matters is how it relates to other elements in the layout. WTF, why can't we position & size elements relative to each other, not just relative to their positioned parents? For more than a decade, web developers have been asking for this, but the W3C refuses to tackle the engineering problems associated with the "cyclic dependencies" that naturally arise in relative layout logic.
{{% /quote %}}


```html
<nav class="nav nav-primary">
  <ul>
    <li class="tab-conversation active">
      <a href="#" data-role="post-count" class="publisher-nav-color" data-nav="conversation">
        <span class="comment-count">0 комментариев</span>
        <span class="comment-count-placeholder">Комментарии</span>
      </a>
    </li>
    <li class="dropdown user-menu" data-role="logout">
      <a href="#" class="dropdown-toggle" data-toggle="dropdown">
        <span class="dropdown-toggle-wrapper">
          <span>
            Войти
          </span>
        </span>
        <span class="caret"></span>
      </a>
    </li>
  </ul>
</nav>
```

