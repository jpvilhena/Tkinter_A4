import React, { useEffect, useMemo, useState } from 'react';

  const fetchOne = async () => {
    if (!searchId.trim()) return;
    setLoading(true);
    setError('');
    setMessage('');
    try {
      const res = await fetch(`${API_BASE}${resource.path}/${encodeURIComponent(searchId.trim())}`);
      if (!res.ok) throw new Error(`GET one failed: ${res.status}`);
      const data = await res.json();
      setSelectedItem(data);
      setPatchJson(safeStringify(data));
    } catch (err) {
      setError(err.message || 'Erro ao buscar item');
    } finally {
      setLoading(false);
    }
  };

  const createItem = async () => {
    setLoading(true);
    setError('');
    setMessage('');
    try {
      const payload = JSON.parse(createJson);
      const res = await fetch(`${API_BASE}${resource.path}/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await res.json().catch(() => null);
      if (!res.ok) throw new Error(data?.detail || `POST failed: ${res.status}`);
      setMessage('Registro criado com sucesso.');
      setCreateJson('{\n  \n}');
      await fetchItems();
    } catch (err) {
      setError(err.message || 'Erro ao criar item');
    } finally {
      setLoading(false);
    }
  };

  const updateItem = async () => {
    if (!selectedItem) {
      setError('Selecione um item primeiro.');
      return;
    }
    setLoading(true);
    setError('');
    setMessage('');
    try {
      const payload = JSON.parse(patchJson);
      const id = selectedItem[resource.idKey];
      const res = await fetch(`${API_BASE}${resource.path}/${encodeURIComponent(id)}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await res.json().catch(() => null);
      if (!res.ok) throw new Error(data?.detail || `PATCH failed: ${res.status}`);
      setMessage('Registro atualizado com sucesso.');
      setSelectedItem(data);
      setPatchJson(safeStringify(data));
      await fetchItems();
    } catch (err) {
      setError(err.message || 'Erro ao atualizar item');
    } finally {
      setLoading(false);
    }
  };

  const deleteItem = async (item) => {
    const id = item?.[resource.idKey];
    if (id === undefined || id === null) return;
    const ok = window.confirm(`Excluir este registro (${resource.idKey}: ${id})?`);
    if (!ok) return;

    setLoading(true);
    setError('');
    setMessage('');
    try {
      const res = await fetch(`${API_BASE}${resource.path}/${encodeURIComponent(id)}`, {
        method: 'DELETE',
      });
      if (!res.ok && res.status !== 204) throw new Error(`DELETE failed: ${res.status}`);
      setMessage('Registro excluído com sucesso.');
      if (selectedItem && selectedItem[resource.idKey] === id) setSelectedItem(null);
      await fetchItems();
    } catch (err) {
      setError(err.message || 'Erro ao excluir item');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto max-w-7xl p-6 lg:p-10">
        <div className="mb-8 rounded-3xl border border-slate-800 bg-slate-900/80 p-6 shadow-2xl">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.25em] text-slate-400">MudaExpress</p>
              <h1 className="mt-2 text-3xl font-semibold">Painel CRUD simples</h1>
              <p className="mt-2 max-w-2xl text-sm text-slate-300">
                Frontend básico para testar listagem, criação, atualização e exclusão nas rotas FastAPI.
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <select
                value={resourceKey}
                onChange={(e) => setResourceKey(e.target.value)}
                className="rounded-2xl border border-slate-700 bg-slate-950 px-4 py-3 text-sm outline-none"
              >
                {RESOURCES.map((r) => (
                  <option key={r.key} value={r.key}>
                    {r.label}
                  </option>
