"""BSD 3-Clause License

Copyright (c) 2019, Charles Kaminski (CharlesKaminski@gmail.com)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
      
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
      
    * Neither the name of the copyright holder nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL CHARLES KAMINSKI BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

class Clusters:
    """Iterator.  Takes a list of dictionary objects with IDs and Parent IDs.
       Returns records grouped into lists based on membership in a tree.  The 
       order of the records does not matter.  This is useful when grouping
       flat records based on tree membership or detecting breaks in a tree.

       usage -> clusters = [x for x in Clusters(records)]
       usage -> clusters = list(Clusters(records))"""

    def __init__(s, records, id_key='id', parent_key='parent'):
        s.idk, s.pk = id_key, parent_key
        s.r = records[:]
        

    def __iter__(s):
        return s    

    def _recurse(s, cr, rl):
        
        # Set local references to ease lookups.
        idk, pk, r = s.idk, s.pk, s.r
        recurse = s._recurse
        
        # add current record to return list
        rl.append(cr)

        # Get current record ID.
        crid = cr[idk]

        # Create object to emit r's indexes in reverse. You have to pop in reverse.
        rev = xrange(len(r)-1,-1,-1)

        # Find children and move them from records.
        c = [r.pop(x) for x in rev if r[x].get(pk, '') == crid]

        # recurse over each child (this climbs down the tree).
        [recurse(x, rl) for x in c]

        # Get parent ID (if exists).
        pid = cr.get(pk, None)
        
        # If parent ID doesn't exist, return list
        if not pid: return rl

        # Create object to emit r's indexes in reverse (to pop in reverse).
        #  A reverse index isn't strictly required this time since next() will 
        #  only pop once.  But consistency here helps in the wild since
        #  parents are often found close to children.
        rev = xrange(len(r)-1,-1,-1)   

        # Find the parent and remove it from records.
        p = next((r.pop(x) for x in rev if r[x].get(idk, '')==pid), None)
        
        # If there's no parent found, return list
        if not p: return rl       
            
        # Recurse over parent and return parent (this climbs up the tree).
        rl = recurse(p, rl)

        # Return list.
        return rl       

    def __next__(s):
        # Python 3.x
        return s.next(s)
    
    def next(s): 
        # Python 2.x
        
        # if there are records, then build a tree.
        if s.r: return s._recurse(s.r.pop(-1), [])
        
        # If there are no more records, then stop iterating.
        raise StopIteration()    

class Trees:
    """Iterator.  Takes a list of dictionary objects with IDs and Parent IDs.
       Returns Trees by recursively placing children as a list in the 
       children key.  Record order does not matter.  Number of trees in the 
       record list does not matter.  The root of each tree will be returned 
       as a separate dictionary object by the iterator.
       
       usage -> trees = [x for x in Trees(records)]
       usage -> trees = list(Trees(records))"""
    
    def __init__(s, records, 
                 id_key='id', parent_key='parent', children_key='children'):
        
        s.idk, s.pk, s.ck = id_key, parent_key, children_key
        s.r = records[:]

    def __iter__(s):
        return s

    def _recurse(s, cr):
        
        # Set local references to ease lookups.
        idk, pk, ck, r = s.idk, s.pk, s.ck, s.r
        recurse = s._recurse

        # Get current record ID.
        crid = cr[idk]

        # Create object to emit r's indexes in reverse. You have to pop in reverse.
        rev = xrange(len(r)-1,-1,-1)

        # Find children and move them from records.  Pop in reverse.
        c = [r.pop(x) for x in rev if r[x].get(pk, '') == crid]

        # Add children into the children section of the current record.
        cr[ck] = cr.get(ck, []) + c

        # recurse over each child (this climbs down the tree).
        [recurse(x) for x in c]

        # Get parent ID (if exists).
        pid = cr.get(pk, None)
        
        # If parent ID doesn't exist, return current record
        if not pid: return cr

        # Create object to emit r's indexes in reverse (to pop in reverse).
        #  A reverse index isn't strictly required this time since next() will 
        #  only pop once.  But consistency here helps in the wild since
        #  parents are often found close to children.
        rev = xrange(len(r)-1,-1,-1)   

        # Find the parent and remove it from records.
        p = next((r.pop(x) for x in rev if r[x].get(idk, '')==pid), None)
        
        # If there's no parent found, return current record
        if not p: return cr
        
        # Add current record to parent's children
        p[ck] = p.get(ck,[]) + [cr]                
            
        # Recurse over parent and return parent (this climbs up the tree).
        cr = recurse(p)

        # Return current record.
        return cr        

    def __next__(s):
        # Python 3.x
        return s.next(s)
    
    def next(s): 
        # Python 2.x
        
        # if there are records, then build a tree.
        if s.r: return s._recurse(s.r.pop(-1))
        
        # If there are no more records, then stop iterating.
        raise StopIteration()

if __name__ == '__main__':
    records = [
        {"id": '1', "parent": ''},     # 1 tree
        {"id": '2', "parent": '1'},  
        {"id": '3', "parent": '2'},
        {"id": '4', "parent": '2'},
        {"id": '5', "parent": '4'},
        {"id": '6', "parent": '99'},   # 2 tree 
        {"id": '7', "parent": '6'},
        {"id": '8', "parent": '7'},
        {"id": '9', "parent": '7'},
        {"id": '10', "parent": '27'},  # 3 tree
        {"id": '11'},                  # 4 tree
        {"id": '12', "parent": '11'},
        {"id": '13', "parent": '11'},
        {"id": '14', "parent": '12'},
        {"id": '15', "parent": '354'}, # 5 tree
    ]
    
    import json 
    import random
    
    print "Records:"
    print json.dumps(records, indent=2)
    
    random.shuffle(records)

    print "Clusters"
    clusters = list(Clusters(records))
    print json.dumps(clusters, indent=2)
    
    print "Trees:"
    trees = list(Trees(records))
    print json.dumps(trees, indent=2)
