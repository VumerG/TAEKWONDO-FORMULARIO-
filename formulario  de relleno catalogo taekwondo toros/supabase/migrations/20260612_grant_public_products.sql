drop policy if exists "Permitir lectura pública" on public.products;
drop policy if exists "Permitir inserción anónima" on public.products;
drop policy if exists "Permitir actualización" on public.products;
drop policy if exists "Permitir eliminación" on public.products;

grant select, insert, update, delete on table public.products to anon;
grant select, insert, update, delete on table public.products to authenticated;
grant select, insert, update, delete on table public.products to service_role;
grant usage, select, update on sequence public.products_id_seq to anon;
grant usage, select, update on sequence public.products_id_seq to authenticated;
grant usage, select, update on sequence public.products_id_seq to service_role;

create policy "Permitir lectura pública" on public.products
for select to anon, authenticated
using (true);

create policy "Permitir inserción anónima" on public.products
for insert to anon, authenticated
with check (true);

create policy "Permitir actualización" on public.products
for update to anon, authenticated, service_role
using (true)
with check (true);

create policy "Permitir eliminación" on public.products
for delete to anon, authenticated, service_role
using (true);
