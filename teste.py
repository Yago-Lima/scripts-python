from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
import time

print('Automação iniciada! Aguarde...')
print('')
print('.')
print('.')
print('.')
print('')

print('Inciando postagem...')
time.sleep(3)

# Substitua 'https://www.seusite.com.br/xmlrpc.php', 'seu-user-aqui', 'qRfsj2Ix0WjnjppG8lMHQ*5O'
# pelos seus dados de autenticação do WordPress
your_blog = Client('https://4sdrive.com.br/xmlrpc.php', 'bot', 'qRfsj2Ix0WjnjppG8lMHQ*5O')

# Substitua 'wpdmpro' pelo seu tipo de post personalizado
post_type = 'wpdmpro'

# Substitua 'FIREFOX O MELHOR NAVEGADOR' e o conteúdo pelo título e texto desejados
TITULO = 'FIREFOX O MELHOR NAVEGADOR'
TEXTO = 'Comece a navegar, e iremos mostrar-lhe alguns dos ótimos artigos, vídeos, e outras páginas que visitou recentemente ou adicionou aos marcadores aqui.'

myposts = your_blog.call(posts.GetPosts())
        
post = WordPressPost()
post.title = TITULO
post.slug = ''
post.content = TEXTO
post.post_status = 'publish'
post.post_type = post_type
post_id = your_blog.call(posts.NewPost(post))
your_blog.call(posts.EditPost(post_id, post))

print('postagem concluída...')
time.sleep(2)

print('') 
print('.')
print('.')
print('.')
print('')
print('Automação concluída com sucesso!')
