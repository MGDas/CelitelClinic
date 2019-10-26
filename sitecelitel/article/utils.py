from tag.models import ArticleTag

def other_articles(tags, object):

    other_articles = []

    if tags:
        for tag in tags:

            article_tag = ArticleTag.pub_objects.get(title=tag.title)

            for article in article_tag.articles.all():
                if len(other_articles) >= 4:
                    break
                if article not in other_articles and article != object:
                    other_articles.append(article)

    return other_articles
