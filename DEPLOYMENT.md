# Despliegue online (gratis y estable)

Este proyecto ya está preparado como sitio estático. La forma más simple y confiable para dejarlo online gratis es:

1. Sube la carpeta completa a GitHub.
2. En GitHub, activa Pages desde la rama `main`.
3. Usa la URL que te genere GitHub Pages.
4. Asegúrate de que la tabla `public.products` exista en Supabase y que las políticas RLS permitan lectura/escritura anónima (el SQL de `supabase/schema.sql` ya está pensado para eso).

## Recomendación
- GitHub Pages: hosting gratis para el frontend.
- Supabase: base de datos y API gratis para el catálogo.

## Qué debes revisar en Supabase
- Proyecto activo.
- Tabla `public.products` creada.
- Políticas RLS habilitadas.
- La clave anónima usada por el frontend está vigente.

## Resultado esperado
- `index.html`: formulario para guardar productos.
- `catalogo.html`: catálogo público para ver productos.

Si quieres un paso adicional de seguridad, luego puedes añadir políticas RLS más estrictas y un backend pequeño para escrituras administradas.
